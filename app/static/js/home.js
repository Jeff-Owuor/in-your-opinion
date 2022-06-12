const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('.rate-form')  
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


const handleStarSelect = (size) =>{
    const children = form.children 
    for (let i=0;i < children.length;i++){
        if(i<=size){
            children[i].classList.add('checked')
        }
        else{
            children[i].classList.remove('checked')
        }
    }
}

const handleSelect = (selection) =>{
    switch(selection){
        case 'first':{
            handleStarSelect(1)
            break
        }
        case 'second':{
            handleStarSelect(2)
            break
        }
        case 'third':{
            handleStarSelect(3)
            break
        }
        case 'fourth':{
            handleStarSelect(4)
            break
        }
        case 'fifth':{
            handleStarSelect(5)
            break
        }
    }
}

const getRatingNumber = (stringRatingValue) =>{
         let ratingValue;
         if(stringRatingValue == "first"){
             ratingValue = 1;
         }else if(stringRatingValue == "second"){
            ratingValue = 2;
        }else if(stringRatingValue == "third"){
            ratingValue = 3;
        }
        else if(stringRatingValue == "fourth"){
            ratingValue = 4;
        }else if(stringRatingValue == "fifth"){
            ratingValue = 5;
        }else{
            ratingValue = 0
        }

        return ratingValue
}

if(one){
    const arr = [one,two,three,four,five]

    arr.forEach(item => item.addEventListener('mouseover', (event) =>  {
        handleSelect(event.target.id)
    }))

    arr.forEach(item => item.addEventListener('click', (event) =>{
         let star_val = event.target.id
         let is_submit = false
          
         form.addEventListener('submit', (e) =>{
              e.preventDefault()
              if (is_submit){
                  return
              }
              is_submit = true
              let imageIdString = e.target.id
              let imageIdNumber = getRatingNumber(imageIdString)

              $.ajax({
                type:'POST',
                url:'/rate/',
                data:{
                    'csrfmiddlewaretoken':csrf[0].value,
                    'element_id':imageIdString, 
                    'val': imageIdNumber
                },
                success: function(response){
                      confirmBox.innerText = `Succesfully rated with ${response.score}` 
                },
                error: function(error){
                       confirmBox.innerText = 'Oops!! something went wrong '
                }
            })
         })
         
    }))
}
