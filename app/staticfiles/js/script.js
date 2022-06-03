if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
};
window.onscroll=function(){
    var st = window.pageYOffset || document.documentElement.scrollTop; 
    if (st > lastScrollTop){
        if (window.pageYOffset >=70) {
            if (window.pageYOffset >=500){
                document.getElementsByClassName("upbutton")[0].style.display="inline-block"
            };
            navb.style.top="0px";
            navb.classList.add("navbarscroll");
        }
        else {
            navb.classList.remove("navbarscroll");
        }
   }
   else {
       if (st < lastScrollTop){
           
           if (window.pageYOffset <=90){
            navb.classList.remove("navbarscroll");
            navb.style.top="0px";
            if (window.innerWidth<800.98){
                document.getElementById("navbar-menu-list").style.left="-100%";
            }
        }
        else{
                navb.style.top="-150px";
            }
       };
       if (window.pageYOffset <=500){
        document.getElementsByClassName("upbutton")[0].style.display="none"
        };
   }
   lastScrollTop = st <= 0 ? 0 : st;
}

function hidenav(){
    if (window.innerWidth<800.98){
        x=document.getElementById("navbar-menu-list")
        x.style.left="-100%";
    }
}
function shownav(){
    x=document.getElementById("navbar-menu-list")
    if(x.style.left==="-100%"){
        x.style.left="0";
    }else{
        x.style.left="-100%";
    }
}

function showthese(n){
    let i;
    let slidess=document.getElementsByClassName("slide");
    for(i = 0; i < slidess.length; i++){
            slidess[i].style.display="none";
    }
    if (window.innerWidth>640.98){
        if (window.innerWidth > 991.98){
            if(n==1){
                slidess[n-1].style.display="block";
                slidess[n].style.display="block";
                slidess[n+1].style.display="block";
            }
            else{
                slidess[n+1].style.display="block";
                slidess[n+2].style.display="block";
                slidess[n+3].style.display="block";
            }
            }
        else{
            if(n==1){
                slidess[n-1].style.display="block";
                slidess[n].style.display="block";
            }
            else if(n == 2){
                slidess[n].style.display="block";
                slidess[n+1].style.display="block";
            }
            else{
                slidess[n+1].style.display="block";
                slidess[n+2].style.display="block";
            }
            }
        }
    else{
        slidess[n-1].style.display="block";
    }
}
function moveup(){
    console.log('moving up');
    window.scrollTo(0, 0);
}
let navb = document.getElementById("navbar");
var lastScrollTop = 0;
let indexslide=1;
slidechange(indexslide)
function slidechange(indexslide){
    showthese(indexslide)
}
function resize()
{
    slidechange(1);
}

window.onresize = resize;
