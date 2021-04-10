let vids= Array.from(document.getElementsByTagName('video'))

for(let v of vids) {
    let src = `feed_${v.attributes['feed-index'].value}/playlist`
    console.log(src)

    if (Hls.isSupported()) {
        let hls = new Hls();
        hls.loadSource(src);
        hls.attachMedia(v);
    } else if (v.canPlayType('application/vnd.apple.mpegurl')) {
        v.src = src;
    }
}

if(window.devicePixelRatio > 1) {
    document.querySelector("#video-grid").style.height= "100%"
}