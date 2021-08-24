const link = document.querySelector('#color')
const words = link.textContent

if (words.includes('successfully')){
    link.style.color = 'green'}

else{
    link.style.color='red'}

