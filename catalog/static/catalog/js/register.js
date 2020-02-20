username_input = document.getElementById('id_username')
email_input = document.getElementById('id_email')
password1_input =document.getElementById('id_password1')
password2_input =document.getElementById('id_password2')

username_helper = document.getElementById('username-helper')
email_helper = document.getElementById('email-helper')
password_helper = document.getElementById('password-helper')

helper = document.getElementById('helper')

function username_helper() {
	helper.innerHTML = "	<p> Letras, dígitos e @, ., +, -, _ . </p>  "
}
