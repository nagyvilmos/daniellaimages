<script>
    export let images;
    export let imageHeight = 150;
    export let imageSpacing = 5;
</script>

<div class="carousel">
    <div class="xcarousel__container">
        {#each images as image (image.id)}
            <img class="image"
                src={image.path}
                alt={image.alt}
                id={image.id}
                xstyle={`height: ${imageHeight}px; margin-right: ${imageSpacing}px`}
            />
        {/each}
    </div>
</div>

<style>
    .carousel {
        display: flex;
        position: relative;
        width: 100%;
        z-index: 1;
    }
    .carousel__container {
        display: flex;
    }
    .image {
        max-width: 30vw;
        max-height: 30vh;
        margin: 4px;
    } 
</style>