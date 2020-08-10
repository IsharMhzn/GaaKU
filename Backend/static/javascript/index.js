
//DOM ELEMENTS

const selectElement =(element)=> document.querySelector(element);
const h_scrolling=document.querySelectorAll(".circle");
const left_scrolling_button=document.querySelector(".left");
const right_scrolling_button=document.querySelector(".right");

const cover_title=document.querySelector('.cover-title');
const cover_text=document.querySelector('.cover-text');
const cover_image=document.querySelector('.cover-image');

selectElement('.menu-icons').addEventListener('click',()=>{
	selectElement('.container-nav').classList.toggle('active');
});

//Variables

let circle_active="col8 circle circle-active";
let circle="col8 circle";
let index;


//Functions
//For Scrolling
let class_present=(array,class_name)=>{
	for(i=0;i<array.length;i++){
		if(array[i].className===class_name){
			return i;
		}
	}
}

function change_template(index){
	switch(index){
		case 0:
		cover_title.innerHTML="Focused on First Years";
		cover_text.innerHTML="Get good qualtity drafters straight from the hands from your trusty 		seniors and make your drawing classes easy and interesting.";
		cover_image.src='/static/image/Drafter.png';
		break;

		case 1:
		cover_title.innerHTML="Focused on Second Years";
		cover_text.innerHTML="Get good qualtity Electronics straight from the hands from your trusty 		seniors and make your drawing classes easy and interesting.";
		cover_image.src="/static/image/Electronics-circle.png"
		break;

		case 2:
		cover_title.innerHTML="Focused on Third Years";
		cover_text.innerHTML="Get good qualtity Furniture straight from the hands from your trusty 		seniors and make your drawing classes easy and interesting.";
		cover_image.src="/static/image/Furniture-circle.png";
		break;

		case 3:
		cover_title.innerHTML="Focused on Fourth Years";
		cover_text.innerHTML="Get good qualtity Musical Instrument straight from the hands from your trusty 		seniors and make your drawing classes easy and interesting.";
		cover_image.src="/static/image/Musical-circle.png";
		break;

		case 4:
		cover_title.innerHTML="Focused on All Years";
		cover_text.innerHTML="Get good qualtity Musical Instrument straight from the hands from your trusty 		seniors and make your drawing classes easy and interesting.";
		cover_image.src="/static/image/books-circle.png"
		break;

		case 5:
		cover_title.innerHTML="Focused on Not All Years";
		cover_text.innerHTML="Get good qualtity Musical Instrument straight from the hands from your trusty 		seniors and make your drawing classes easy and interesting.";
		cover_image.src="/static/image/Shoes-circle.png";
		break;
		default:
		break;
	}
}

let index_position=(array,position_shift)=>{
	index=class_present(array,circle_active);
	array[index].className=circle;
	if(position_shift==="right"){
		index=(index+1)%array.length;
	}
	else{
		index=(index-1)%array.length;
	}
	if(index<0){
		index=array.length-1;
	}
	array[index].className=circle_active;
	change_template(index);
}

right_scrolling_button.addEventListener('click',function(){
	index_position(h_scrolling,"right");
});

left_scrolling_button.addEventListener('click',function(){
	index_position(h_scrolling,"left");
});