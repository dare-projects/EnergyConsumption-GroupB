library(ggplot2)
library(chron)
library(dplyr)
library(plyr)
library(mgcv)

clean_df <- function(df){
  #change columns name
  names(df)[1] = 'Date'
  names(df)[3] = 'Quality'
  names(df)[4] = 'Status'
  #format date
  df$Date <- as.chron(df$Date, '%Y-%m-%d %H:%M:%S')
  #select valid data
  df <- df %>% filter(df$Quality == 'Real', df$Status == 'Valid')
  #remove outliers
  if(names(df)[2] != 'Irradiance'){
    df <- filter(df, !(df[,2] %in% boxplot.stats(df[,2])$out))
  }
  #return only dates and values
  return(df[, 1:2])
}

#load datasets
df1 <- read.csv('./EnSig_2018_Genn_Apr.csv', stringsAsFactors = FALSE)
df2 <- read.csv('./EnSig_2018_Magg_Ago.csv', stringsAsFactors = FALSE)
df3 <- read.csv('./EnSig_2018_Sett_Dic.csv', stringsAsFactors = FALSE)
df4 <- read.csv('./EnSig_2017_Jan_Apr.csv', stringsAsFactors = FALSE)
df5 <- read.csv('./EnSig_2017_May_Sep.csv', stringsAsFactors = FALSE)
df6 <- read.csv('./EnSig_2017_Sep_Dec.csv', stringsAsFactors = FALSE)

#concatenate datasets
ds <- rbind(df1, df2, df3, df4, df5, df6)

#split into 4 datasets based on feature
irr <- ds[0:4]
en <- ds[5:8]
ext <- ds[9:12]
off <- ds[13:16]

#clean dataframes
irr <- clean_df(irr)
en <- clean_df(en)
ext <- clean_df(ext)
off <- clean_df(off)

#join dataframes
final <- inner_join(irr, en, on='Date')
final <- inner_join(final, ext, on='Date')
final <- inner_join(final, off, on='Date')

#delta temperature
#negative if ext is cooler than off, positive otherwise
final$Delta_Temperature <- final$External_Temperature - final$Office_Temperature

#day of the week
final$Day <- weekdays(final$Date)
final$Day <- mapvalues(final$Day, from = c('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'), to = seq(1:7))
final$Day <- as.numeric(final$Day)

#month
final$Month <- months(final$Date)
final$Month <- mapvalues(final$Month,from = c('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'),to = seq(1:12))
final$Month <- as.numeric(final$Month)
#hours
final$Hours <- hours(final$Date)

#working
final$Working <- ifelse((final$Day <= 5 & final$Hours >= 7 & final$Hours <= 20), 1, 0)

#remove date
final <- final[, c('Irradiance', 'Delta_Temperature', 'Day', 'Month', 'Hours', 'Working', 'Energy', 'Office_Temperature', 'External_Temperature')]

#export to csv
write.csv(final, 'C:/Users/Giacomo Rocchetti/Desktop/EnergySignature/dataset.csv')
