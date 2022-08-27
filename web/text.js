 async function msg(){
            let result = await eel.t();
            document.getElementByid('ad').innerHTML = result;
        }

        $('#submit').click(function(){
            msg();
        });