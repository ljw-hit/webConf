

function addLink(checkbox){
  if(checkbox.checked){
     link.push(checkbox.value)
  }else{
   link.pop(checkbox.value)
  }
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
                        console.log(res);
                    }
    });
}