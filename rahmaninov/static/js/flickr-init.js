/**
 * Created by nani on 11/11/13.
 */

$(function () {
    var apiKey = 'c1f877b4f6f168f6cc90d03e73ca47be';
    var images = $("#footer-photos").find('img');
    $.getJSON('http://api.flickr.com/services/rest/', {
        method: 'flickr.photos.search',
        api_key: apiKey,
        user_id: '65968911@N08',
        tags: 'rahmaninov',
        privacy_filter: 1,
        content_type: 1,
        extras: 'url_m',
        format: 'json',
        nojsoncallback: 1
    }).done(function (data) {
            var horizontal = data.photos.photo.filter(function (item) {
                if (item.width_m == 500 && item.height_m == 333) {
                    return true;
                }
            }).slice(0, 6);
            $.each(horizontal, function (j, item) {
                images[j].src = item.url_m;
            });
        });
});