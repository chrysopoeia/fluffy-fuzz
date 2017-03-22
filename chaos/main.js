(function(){
    // super uber ultra mega incredible images (yes, sue me)
    var suumii = [
	'http://i.imgur.com/grGMGAy.gif',
	'https://s3.amazonaws.com/gs-geo-images/694ef333-7c4e-4e2a-87e2-ec31fb814540.jpg',
	'https://upload.wikimedia.org/wikipedia/en/7/72/Mark_Wing-Davey_as_Zaphod_Beeblebrox.jpg',
	'https://media.giphy.com/media/FafwmLLfoCad2/giphy.gif',
	'https://s-media-cache-ak0.pinimg.com/600x315/c3/af/cd/c3afcd6370e9056a1b5c47dfa83f3b9d.jpg',
	'https://cdn1.lockerdome.com/uploads/6853d4e5023f208b2fde06a7f83d7e85e856b60765e8c91217eebd074ad69bf5_medium_animated',
    ];
    
    var all = document.body.getElementsByTagName('*');
    for (var i = 0; i < all.length; i++)
    {
	new Chaotic(all[i]);
    }
    
    function Chaotic(el)
    {
	var delay = 40;
	var thread_id = undefined;
	var rotation = 0;
	var rotation_rate = 0;
	var iterations = 0;
	
	if (el.tagName == 'IMG')
	{
    	    el.width = el.offsetWidth;
    	    el.height = el.offsetHeight;
	    el.style.width = el.width + 'px';
	    el.style.height = el.height + 'px';
    	    el.src = suumii[parseInt(Math.random() * suumii.length*3)] || el.src;
	}
	
	function mouseover(evt)
	{
	    evt.stopPropagation();
	    
	    thread_id = setInterval(function(){
		rotation_rate += 0.5 - Math.random();
		rotation = (rotation + rotation_rate) % 360;
		
		skewx = Math.sin(iterations/2) * 10;
		skewy = Math.sin(iterations/2) * 10;
		
		el.style.transform = 'rotate('+rotation+'deg) skewX('+skewx+'deg) skewY('+skewy+'deg)';
		
		iterations += 1
	    }, delay)
	}
	
	function mouseout(evt)
	{
	    thread_id = clearInterval(thread_id);
	}
	
	el.addEventListener('mouseover', mouseover);
	el.addEventListener('mouseout', mouseout);
    }

})();
