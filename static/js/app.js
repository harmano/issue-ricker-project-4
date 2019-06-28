$(document).ready(function() {
            var chip = {
              tag: 'chip content',
              image: '', //optional
            };
            $('.collapsible').collapsible();
            $('select').material_select();
            $('.materialboxed').materialbox();
            $(".button-collapse").sideNav();
            $('.slider').slider();
            $('.chips').chips();
            $('.tooltipped').tooltip();
        });