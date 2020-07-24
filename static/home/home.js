burger = document.querySelector('.burger');
navlist = document.querySelector('.nav-list');
navbar = document.querySelector('#navbar');

burger.addEventListener('click', ()=>{
    navlist.classList.toggle('v-nav');
    navbar.classList.toggle('h-nav');
})