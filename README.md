# Databases-and-Data-Mining-Project
 Our project interprets internet use, homicide rates and population size for countries around the world from 1990-2014 to see what, if any, relationships exist between these factors. The central, initial question that piqued our curiosity was whether internet use is linked to homicide rates. Perhaps high internet use signified a more highly educated population, and so there would be less crime (or maybe people were spending more time watching cat videos than plotting a crime). Or, perhaps more internet use would mean more access to violent content and forums for violent communities, resulting in higher homicide rates. We set out to build a model that would allow us to determine what, if any, link exists. Ultimately, when we ran our data in Weka, we found that the highest indicator of homicide rate was population. This makes sense: as population rises, you’d expect homicide to rise proportionally. However, since this model did not answer our central curiosity as to whether there was a link between internet use and homicide rates, we also ran our data in R, another statistical tool. R presented us with a model showing higher internet use as linked with lower homicide rates. Our theory of high internet use indicating a more educated, civilized culture with less homicide held. However, the p-value of this model was quite high, indicating that this seemingly potential link - and theory - is insignificant.
