//DOM ELEMENTS

const selectElement =(element)=> document.querySelector(element);
const h_scrolling=document.querySelectorAll(".circle");
const left_scrolling_button=document.querySelector(".left");
const right_scrolling_button=document.querySelector(".right");

const cover_title=document.querySelector('.cover-title');
const cover_text=document.querySelector('.cover-text');
const cover_image=document.querySelector('.cover-image');
const cover_image_first=document.querySelector('.first');
const ad_wrapper=document.querySelector('.ad-wrapper');
const ad_image=document.querySelectorAll('.ad-col2 img');

const content1=document.getElementById('content1');
const content2=document.getElementById('content2');
const content3=document.getElementById('content3');
const content=document.querySelector('.content');

selectElement('.menu-icons').addEventListener('click',()=>{
	selectElement('.container-nav').classList.toggle('active');
});

//Variables

let circle_active="col8 circle circle-active";
let circle="col8 circle";
let index;
let scroll_index=1;

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

function image_resize(){
	for(i=0;i<ad_image.length;i++){
		console.log(ad_image[i].clientHeight);
	}
}

function element_resize(element1,element2){
	height=element1.clientHeight.toString();
  	element2.style.height=height+"px";
}


right_scrolling_button.addEventListener('click',function(){
	index_position(h_scrolling,"right");
});

left_scrolling_button.addEventListener('click',function(){
	index_position(h_scrolling,"left");
});


setInterval(function(){
	index_position(h_scrolling,"right");
	scroll_index++;
	if(scroll_index>3){
		scroll_index=1;
	}
	switch(scroll_index){
		
		case 1:
			content1.style.transform="translateX(0px)";
			content2.style.transform="translateX(150%)";
			content3.style.transform="translateX(150%)";
			content1.style.transitionDelay="0.3s";
			content2.style.transitionDelay="0s";
			content3.style.transitionDelay="0s";
		break;
		case 2:
			content1.style.transform="translateX(150%)";
			content2.style.transform="translateX(0px)";
			content3.style.transform="translateX(150%)";
			content1.style.transitionDelay="0s";
			content2.style.transitionDelay="0.3s";
			content3.style.transitionDelay="0s";
		break;
		case 3:
			content1.style.transform="translateX(150%)";
			content2.style.transform="translateX(150%)";
			content3.style.transform="translateX(0px";
			content1.style.transitionDelay="0s";
			content2.style.transitionDelay="0s";
			content3.style.transitionDelay="0.3s";
		break;
	}
},5000);


element_resize(content,ad_wrapper);

$(window).resize(function() {
  console.log('window was resized');
  resize(content,ad_wrapper)
});