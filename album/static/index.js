document.addEventListener("DOMContentLoaded", function(event) {

    const showNavbar = (toggleId, navId, bodyId, headerId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId),
    bodypd = document.getElementById(bodyId),
    headerpd = document.getElementById(headerId)
    
    if(toggle && nav && bodypd && headerpd){
    toggle.addEventListener('click', ()=>{
    // show navbar
    nav.classList.toggle('show')
    // change icon
    toggle.classList.toggle('bx-x')
    // add padding to body
    bodypd.classList.toggle('body-pd')
    // add padding to header
    headerpd.classList.toggle('body-pd')
    })
    }
    }
    
    showNavbar('header-toggle','nav-bar','body-pd','header')
    
    const linkColor = document.querySelectorAll('.nav_link')
    
    function colorLink(){
    if(linkColor){
    linkColor.forEach(l=> l.classList.remove('active'))
    this.classList.add('active')
    }
    }
    linkColor.forEach(l=> l.addEventListener('click', colorLink))
    });

   $(document).on("click", ".open-incident", function (e) {
    e.preventDefault();
    var $popup = $("#popup");
    var popup_url = $(this).data("popup-url");
    $(".modal-body", $popup).load(popup_url, function () {
      $popup.modal("show");
    });
  });
  document.addEventListener('DOMContentLoaded',function(e){
    let field = document.querySelector('.field');
    let input = document.querySelector('input');
    let copyBtn = document.querySelector('.copyLink');
    
    copyBtn.onclick = () =>{
    input.select();
    if(navigator.clipboard("copy")){
    field.classList.add('active');
    copyBtn.innerText = 'Copied';
    setTimeout(()=>{
    field.classList.remove('active');
    copyBtn.innerText = 'Copy';
    },3500)
    }
    }
    })
    function copyLink() {
        /* Get the text field */
        var copyText = document.getElementById("input");
        var copyBtn = document.getElementById("buttonc");
        copyText.select();
        copyText.setSelectionRange(0, 99999); 
      
         /* Copy the text inside the text field */
        navigator.clipboard.writeText(copyText.value);
      
        /* Alert the copied text */
        copyBtn.innerText = 'Copied';
        setTimeout(()=>{
            copyBtn.innerText = 'Copy';
            },3500)

      }