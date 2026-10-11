(function(){
  function init(root){
    root.querySelectorAll('.pc-trigger').forEach(function(button){
      if(button.dataset.pcReady)return;
      button.dataset.pcReady='1';
      button.addEventListener('click',function(){
        var item=button.closest('.pc-item'); var open=item.classList.toggle('is-open');
        button.setAttribute('aria-expanded',String(open));
      });
    });
  }
  function boot(){document.querySelectorAll('.pc-site').forEach(init)}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();
})();
