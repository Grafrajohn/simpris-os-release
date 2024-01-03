    jQuery(function () {
    jQuery(".gantt").gantt({
        source: "<?php echo base_url() . 'json/' . $ganttData ?>", 
        months: [
                    "January", "February", "March", 
                    "April", "May", "June", "July", 
                    "August", "September", "October", 
                    "November", "December"], 
        dow: ["S", "M", "T", "W", "Th", "F", "Sa"],        
        navigate: 'scroll', 
        scale: 'days', 
        maxScale: 'weeks', 
        minScale: 'days'
        })
    });