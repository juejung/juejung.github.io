# Juergen JUng, July 2012


rm(list=ls()) # Remove almost everything in the memory
require(knitr)      # required for knitting from rmd to md
require(markdown)   # required for md to html

rm(list=ls()) # Remove almost everything in the memory
setwd("~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/Lecture2/R")
print(paste("My current working directory is:",getwd()),quote=FALSE)


# -------------------------------------------------------------------------
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "CourseStructure"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "CourseStructure"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')

# i = "Lecture1/Slides/Slides1_Basics"
# i = "Lecture1/Slides/Slides1_Basics"
# i = "Lecture2/Slides/Slides2_Plot_R"
# i = "Lecture2/Slides/Slides2_Plot_Python"
# i = "Lecture3/Slides/Slides3_Loop_R"
# i = "Lecture3/Slides/Slides3_Loop_Python"
# i = "Lecture4/Slides/Slides4_Data_R"
# i = "Lecture4/Slides/Slides4_Data_Python"
# i = "Lecture5/Slides/Slides5_Functions"
# i = "Lecture6/Slides/Slides6_Matrix_R"
# i = "Lecture6/Slides/Slides6_Matrix_Python"
# i = "Lecture7/Slides/Slides7_Random_R"
# i = "Lecture7/Slides/Slides7_Random_Python"
# i = "Lecture8/Slides/Slides8_Root_R"
# i = "Lecture8/Slides/Slides8_Root_Python"
# i = "Lecture9/Slides/Slides9_Optimization_R"
# i = "Lecture9/Slides/Slides9_Optimization_Python"
# i = "Lecture10/Slides/Slides10_Cake_R"


myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture1/Slides/Slides1_Basics"
  # Step 1: creates .rmd -> .md file
  j_in = paste(myDir, i, ".Rmd",sep = "")
  j_out1= paste(myDir, i, ".md",sep = "")
  knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture1/Slides/Slides1_Basics"
  # Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
  j_out2= paste(myDir, i, ".html",sep = "")
  markdownToHTML(j_out1,j_out2,
  stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')
  
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture2/Slides/Slides2_Plot_R"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture2/Slides/Slides2_Plot_R"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')


myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture2/Slides/Slides2_Plot_Python"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture2/Slides/Slides2_Plot_Python"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')


myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture3/Slides/Slides3_Loop_R"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture3/Slides/Slides3_Loop_R"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')


myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture3/Slides/Slides3_Loop_Python"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture3/Slides/Slides3_Loop_Python"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')


myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture4/Slides/Slides4_Data_R"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture4/Slides/Slides4_Data_R"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')


myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture4/Slides/Slides4_Data_Python"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture4/Slides/Slides4_Data_Python"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')


myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture5/Slides/Slides5_Functions"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture5/Slides/Slides5_Functions"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')


myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture6/Slides/Slides6_Matrix_R"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture6/Slides/Slides6_Matrix_R"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')


myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture6/Slides/Slides6_Matrix_Python"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture6/Slides/Slides6_Matrix_Python"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')


myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture7/Slides/Slides7_Random_R"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture7/Slides/Slides7_Random_R"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')

myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture7/Slides/Slides7_Random_Python"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture7/Slides/Slides7_Random_Python"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')

myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture8/Slides/Slides8_Root_R"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture8/Slides/Slides8_Root_R"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')

myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture8/Slides/Slides8_Root_Python"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture8/Slides/Slides8_Root_Python"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')

myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture9/Slides/Slides9_Optimization_R"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture9/Slides/Slides9_Optimization_R"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')

myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture9/Slides/Slides9_Optimization_Python"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture9/Slides/Slides9_Optimization_Python"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')



myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture10/Slides/Slides10_Cake"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture10/Slides/Slides10_Cake"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')
# make beamer slides
myDirtemp = paste(myDir, 'Lecture10/Slides',sep="")
setwd(myDirtemp)
system("pandoc -t beamer Slides10_Cake.md -V theme:Warsaw -o Slides10_Cake.pdf")
system("pandoc  -t slidy -s -m --mathml Slides10_Cake.md -o Slides10_Cake.html")


myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture11/Slides/Slides11_OLG_I"
# Step 1: creates .rmd -> .md file
j_in = paste(myDir, i, ".Rmd",sep = "")
j_out1= paste(myDir, i, ".md",sep = "")
knit(j_in, j_out1)
myDir = "~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/"
i = "Lecture11/Slides/Slides11_OLG_I"
# Step 2:creates .md ->  .html file
j_out1= paste(myDir, i, ".md",sep = "")
j_out2= paste(myDir, i, ".html",sep = "")
markdownToHTML(j_out1,j_out2,
               stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')
# make beamer slides
myDirtemp = paste(myDir, 'Lecture10/Slides',sep="")
setwd(myDirtemp)
system("pandoc -t beamer Slides11_OLG_I.md -V theme:Warsaw -o Slides11_OLG_I.pdf")
system("pandoc  -t slidy -s -m --mathml Slides11_OLG_I.md -o Slides11_OLG_I.html")























# knit2html(j_in, j_out2)

#c('hard_wrap', 'use_xhtml', 'smartypants',  'base64_images', 'mathjax', 'highlight_code')

# markdownToHTML(j_out1, j_out2,
#                options=c('use_xhml', 'base64_images'),
#                stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')


# markdownToHTML(j_out1, j_out2,
#                stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')# creates .md ->  .html file

# options(encoding='ISO8859-1')
# options(markdown.HTML.options=c("hard_wrap","use_xhtml","smartypants","base64_images","mathjax"))





# for (i in clist) {
#   j_in = paste(myDir, i, ".rmd",sep = "")
#   j_out1= paste(myDir, i, ".md",sep = "")
#   j_out2= paste(myDir, i, ".html",sep = "")
#   #
#   knit(j_in, j_out1)                      # creates .rmd -> .md file
#   markdownToHTML(j_out1, j_out2)          # creates .md ->  .html file
# }

# options(rstudio.markdownToHTML = 
#   function(inputFile, outputFile) {      
#     require(markdown)
#     markdownToHTML(inputFile, outputFile, stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')   
#   }
# )