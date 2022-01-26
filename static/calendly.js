Calendly.initInlineWidget({
    url: 'https://calendly.com/YOURLINK',
    parentElement: document.getElementById('SAMPLEdivID'),
    prefill: {},
    utm: {}
   });

function isCalendlyEvent(e) {
    return e.data.event && e.data.event.indexOf('calendly') === 0;
};
    
window.addEventListener(
    'message',
    function(e) {
    if (isCalendlyEvent(e)) {
        console.log(e.data);
    }
    }
);