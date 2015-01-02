# Run this from within R-Studio, before pressing the Knit HTML button.
# It will then guide the 'markdown.r' package to use pandoc instead of markdownToHTML
# which will allow for the slide show options

# Careful, some of the .rmd commands won't work, like the table function!
# Also Python code chunks seems troublesome as they are not separated by empty-lines in the knitr produced .md file :-(

options(rstudio.markdownToHTML = 
   function(inputFile, outputFile) {      
      system(paste("pandoc  -t slidy -s -m", inputFile, "-o", outputFile))
      #system(paste("pandoc  -t dzslides -s", inputFile, "-o", outputFile))
      #system(paste("pandoc  -t slidy -s", inputFile, "-o", outputFile))
      
   }
) 


#Default:
options(rstudio.markdownToHTML = 
   function(inputFile, outputFile) {      
      require(markdown)
      markdownToHTML(inputFile, outputFile)   
   }
)

# Custom css file
options(rstudio.markdownToHTML = 
   function(inputFile, outputFile) {      
      require(markdown)
      markdownToHTML(inputFile, outputFile,stylesheet='~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/jcssLinux.css')   
   }
)

# If you want to produce beamer slides from the markdown .md file, you can simply run:
# pandoc -t beamer Slides10_Econ_I_R.md -V theme:Warsaw -o Slides10_Econ_I_R.pdf
# pandoc Slides10_Econ_I_R.md -o Slides10_Econ_I_R.pdf
# pandoc Slides2_Plot_R.md -o Slides2_Plot_R.pdf
# pandoc -t beamer Slides2_Plot_R.md -V theme:Warsaw -o Slides2_Plot_R.pdf