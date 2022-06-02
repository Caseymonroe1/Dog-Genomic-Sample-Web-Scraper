#libraries
library(datasets)  
library(ggplot2)
library(tidyverse)
library(plotrix)
library(dplyr)
library(tidytext)
#Setting parameters
par(mar=c(5,11,4,1))
par(mfrow=c(2,2))

#setting up data
dogSample <- import("C:/Users/casey/OneDrive/Desktop/Rtest/samples.csv")
head(dogSample)
summary(dogSample)
breedbars<-table(dogSample$Breed)
genders<-table(dogSample$Gender)
idats<-table(dogSample$`IDAT or not`)
mytable <- table(dogSample$Gender)
lbls <- paste(names(mytable), "\n", mytable, sep="")


#Making plots 
pie3D(mytable, labels = lbls,
      cex=1.2,
      rad=0.9,
      col=c("Red","Blue","Grey"),
      main="Pie Chart of Listed Gender"
      )


barplot(sort(breedbars, decreasing = TRUE)[1:10],
        col="BLACK",
        xlab="Occurences",
        
        xlim=c(0,350),
        las=1,
        horiz=TRUE,
        main="Occurences by Breed",
)

barplot(idats, 
        xlab="IDAT or not",
        ylab="Frequency",
        main="Frequency of IDAT vs Not IDAT",
        ylim=c(0,2500),
        col=c("blue","black")
)
percentages<-c(65.6,34.4)

barplot(percentages,
        main="IDAT vs Not IDAT with percentage",
        ylab="Percentage",
        names.arg=c("IDAT","Not IDAT"),
        col=c("blue","black"),
        ylim=c(0,100)
)
# Clear everything
detach("package:datasets", unload = TRUE)
dev.off()
cat("\014")
