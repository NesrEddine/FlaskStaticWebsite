function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en', includedLanguages: 'ar,en,fr', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
}

$(document).ready(function() {
    $('#idSignIn').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
         feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh' 
        },
		
		
		fields: { 
			
		  name: {
                validators: {
                        stringLength: {
                        min: 6,       },
						
						notEmpty:{
							message: 'Please enter your name'
							}
				
							} 
           		 },
			
            password: {
                validators: {
                        stringLength: {
                        min: 6,       }
				
							} 
           		 },
				 
				 
	         confirmpassword: { 
                validators: {
                        stringLength: {
                        min: 6	,       },
						identical: {
                    field: 'password',
                    message: 'The password and its confirm are not the same'
                }
				
							} 
           		 },
				 
				 
     

		  			 
			
		 email: {
                validators: {
                    notEmpty: {
                        message: 'Please enter your email address'
                    },
                    emailAddress: {
                        message: 'Please enter a valid email address'
                    }
                }
            }, 
			
			
		 message: {  
                validators: {
                        stringLength: {
                        min: 10,
						max:150,       },
				 notEmpty:{
					 message: 'Please enter your message here'
					 }
				
							} 
           		 },
				   
                  
            }
        })
 	
        .on('success.form.bv', function(e) {
            $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
                $('#idSignIn').data('bootstrapValidator').resetForm();

            // Prevent form submission
            e.preventDefault();

            // Get the form instance
            var $form = $(e.target); 

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

            // Use Ajax to submit form data
            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json'); 
        });
});
