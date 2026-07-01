/* Menú móvil accesible */
(function(){
  var t=document.querySelector('.nav-toggle'),m=document.getElementById('menu');
  function closeMenu(focusBtn){if(m){m.classList.remove('open');}if(t){t.setAttribute('aria-expanded','false');}if(focusBtn&&t){t.focus();}}
  if(t&&m){
    t.addEventListener('click',function(){
      var open=m.classList.toggle('open');
      t.setAttribute('aria-expanded',open?'true':'false');
    });
    m.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){closeMenu(false);});});
    document.addEventListener('keydown',function(e){
      if(e.key==='Escape'&&m.classList.contains('open')){closeMenu(true);}
    });
  }
  /* Año dinámico */
  var y=document.getElementById('year');if(y){y.textContent=new Date().getFullYear();}

  /* Formulario (demo: sin backend real — sustituir por endpoint en producción) */
  var f=document.getElementById('contact-form');
  if(f){
    var status=document.getElementById('form-status');
    var btn=f.querySelector('button[type=submit]');
    var fields=[f.name,f.email,f.message,f.consent];
    fields.forEach(function(el){if(el){el.addEventListener('input',function(){
      if(el.checkValidity()){el.removeAttribute('aria-invalid');}
    });}});
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var firstInvalid=null;
      fields.forEach(function(el){
        if(!el)return;
        if(!el.checkValidity()){el.setAttribute('aria-invalid','true');if(!firstInvalid){firstInvalid=el;}}
        else{el.removeAttribute('aria-invalid');}
      });
      if(firstInvalid){
        status.className='form-status err';
        status.textContent='Revisa los campos obligatorios: nombre, email, mensaje y la aceptación de la política de privacidad.';
        firstInvalid.focus();
        return;
      }
      status.className='form-status ok';
      status.textContent='¡Gracias! Hemos recibido tu consulta y te responderemos lo antes posible.';
      btn.textContent='Consulta enviada ✓';
      btn.disabled=true;
      f.reset();
      status.focus();
    });
  }
})();
