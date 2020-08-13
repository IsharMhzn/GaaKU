//DOM ELEMENTS

const selectElement =(element)=> document.querySelector(element);
const h_scrolling=document.querySelectorAll(".circle");
const left_scrolling_button=document.querySelector(".left");
const right_scrolling_button=document.querySelector(".right");

const cover_title=document.querySelector('.cover-title');
const cover_text=document.querySelector('.cover-text');
const cover_image=document.querySelector('.cover-image');
const cover_image_first=document.querySelector('.first');

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
		cover_image_first.style.marginLeft="0%";
		break;

		case 1:
		cover_title.innerHTML="Focused on Second Years";
		cover_text.innerHTML="Get good qualtity Electronics straight from the hands from your trusty 		seniors and make your drawing classes easy and interesting.";
		cover_image_first.style.marginLeft="-111.3%";
		break;

		case 2:
		cover_title.innerHTML="Focused on Third Years";
		cover_text.innerHTML="Get good qualtity Furniture straight from the hands from your trusty 		seniors and make your drawing classes easy and interesting.";
		cover_image_first.style.marginLeft="-222.4%";
		break;

		case 3:
		cover_title.innerHTML="Focused on Fourth Years";
		cover_text.innerHTML="Get good qualtity Musical Instrument straight from the hands from your trusty 		seniors and make your drawing classes easy and interesting.";
		cover_image_first.style.marginLeft="-333.4%";
		break;

		case 4:
		cover_title.innerHTML="Focused on All Years";
		cover_text.innerHTML="Get good qualtity Musical Instrument straight from the hands from your trusty 		seniors and make your drawing classes easy and interesting.";
		cover_image_first.style.marginLeft="-444.4%";
		break;

		case 5:
		cover_title.innerHTML="Focused on Not All Years";
		cover_text.innerHTML="Get good qualtity Musical Instrument straight from the hands from your trusty 		seniors and make your drawing classes easy and interesting.";
		cover_image_first.style.marginLeft="-555.4%";
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

setInterval(function(){
	index_position(h_scrolling,"right");
},5000);
