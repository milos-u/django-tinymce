function djangoFileBrowser(callback, value, meta) {
    var url = "{{ fb_url }}?pop=5&type=" + meta.filetype;

    const instanceApi = tinyMCE.activeEditor.windowManager.openUrl(
        {
            'title': "",
            'url': url,
            'width': 1024,
            'height': 800,
            'onMessage': function (dialogApi, details) {
                callback(details.content)
                instanceApi.close()
            }
        },
    );
    return false
}
