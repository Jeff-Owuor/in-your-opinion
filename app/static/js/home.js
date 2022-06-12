const one = document.getElementById('first')
const two = document.querySelector('#second')
const three = document.querySelector('#third')
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

const arr = [one,two,three,four,five]