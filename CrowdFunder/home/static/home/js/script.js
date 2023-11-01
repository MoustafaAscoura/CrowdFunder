$(document).ready(function(){
    $("#donate_now").click(function(event){
        $("#dform").removeAttr("hidden")
        $("#donate_now").hide()
    })

    $('#show_comment_form').click(function(event){
        $('#comment_form').removeAttr("hidden")
        $('#show_comment_form').hide()
    })

    $('#comment_form button[type=button]').click(function(event){
        $('#comment_form').attr("hidden",true)
        $('#show_comment_form').show()
    })

    $('button.reply').click(function(event){
        
        // comment_id = $(event.target).attr('comment_id');
        let  comment_id = this.getAttribute('comment_id');
        form = document.getElementById(comment_id)
        form.toggleAttribute("hidden")
    })

    $('form.user-form div.mb-3 label').addClass('form-label')
    $('form.user-form div.mb-3 input').addClass("form-control");
    $('form.user-form div.mb-3 select').addClass("form-select");
    $('form.user-form div.mb-3 ul.errorlist li').addClass("text-danger")

    $('#myModal').on('shown.bs.modal', function () {
        $('#myInput').trigger('focus')
    })

    
})
          
$('a.featured').click(function(e){
    console.log(this.getAttribute('href'))
    e.preventDefault()
    $.ajax({
      url: this.getAttribute('href'),
      type: "GET",
    });
    this.firstElementChild.classList.toggle('fa-solid')
    this.firstElementChild.classList.toggle('fa-regular')
  })