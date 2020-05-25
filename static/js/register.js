// Añade estilo css a elementos en register
var form_fields = document.getElementsByTagName('input');
for (var i = form_fields.length - 1; i >= 0; i--) {
	form_fields[i].classList.add('form-control');
}
// Añade los place holder a contraseña
form_fields[3].placeholder='Contraseña';
form_fields[4].placeholder='Repetir contraseña';
