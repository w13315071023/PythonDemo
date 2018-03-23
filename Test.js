


if (data.eventType == "blur") {
    var i = data.dataCustom;
    var ind = parseInt(i.ind);
    var val = i.val;
    elem.querySelector("#random_form").querySelectorAll("td")[ind].querySelector("input").value = val;
  }

  onBlur:function(e){
    var target=e.target;
    var handler=this.props.customHandler;
    if(handler){
      handler({
        data:{val:target.value,ind:target.getAttribute("data-index")},
        eventType:"blur"
      })
    }
  },