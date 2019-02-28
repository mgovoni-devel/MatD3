function alert_submit(form, feedback) {
    form.on('submit', function(event){
        event.preventDefault();
        var data = new FormData(form.get(0));
        $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            data: data,
            cache: false,
            processData: false,
            contentType: false,
            success: function(data) {
                if(data.feedback == "success") {
                    form.each(function(){this.reset();});
                    feedback.html(
                        "<br><p class=\"alert alert-success\" role=\"alert\">"+data.text+"</p>"
                    );
                } else {
                    form.each(function(){this.reset();});
                    feedback.html(
                        "<br><p class=\"alert alert-warning\" role=\"alert\">"+data.text+"</p>"
                    );
                }
            },
            error: function(error) {
                feedback.html(
                    "<br><p class=\"alert alert-danger\" role=\"alert\">Something went wrong, please <a class=\"alert-link\" href=" + window.location.href + ">refresh</a> the page and try again.</p>"
                );
            },
        })
    });
}
