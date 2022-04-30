function checkSelected(){
     let choices = document.getElementsByName('choice_id');
     for(let choice in choices) {
         if(choice.checked){
            return true;
         }
     }
     return alert('NO');
}