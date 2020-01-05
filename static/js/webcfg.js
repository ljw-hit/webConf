

function addLink(checkbox){
  if(checkbox.checked){
     link.push(checkbox.value)
  }else{
   link.pop(checkbox.value)
  }
}
function webSpeed(){
         var element = window.document.getElementById("sp");
          element.innerHTML=parseInt((Math.random()+1)*100)+"KB/s"
}


function startProxy(){
    console.log(link)
    $.ajax({
                    type: 'GET',
                    url: './startProxy/?Data='+link,
//                    data : {
//                             'Data' : link
//                           },
                    success : function(res){
                        // 请求成功
                        console.log("")
                        console.log(res.data);
                        linkmess = res.data
                        var element = window.document.getElementById("lm");
                        element.innerHTML=linkmess;
                    }
    });
}


function getdelay(){
    console.log(link)
    $.ajax({
                    type: 'GET',
                    url: './delay/?Data='+link,
//                    data : {
//                             'Data' : link
//                           },
                    success : function(res){
                        // 请求成功
                        console.log(res.data);
                        linkmess = res.data
                        var element = window.document.getElementById("dt");
                        element.innerHTML=linkmess;
                    }
    });
}