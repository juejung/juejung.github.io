# Run this from within R-Studio, before pressing the Knit HTML button.
# It will then guide the 'markdown.r' package to the user defined 
# jcss.css file in the Dropbox directory

options(rstudio.markdownToHTML = 
  function(inputFile, outputFile) {      
    require(markdown)
    markdownToHTML(inputFile, outputFile, stylesheet='C:/Dropbox/Towson/Teaching/3_ComputationalEconomics/Lectures/jcss.css')   
  }
)

