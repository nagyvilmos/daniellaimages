<script>
    export let images;
    export let imageHeight = 150;
    export let imageSpacing = 5;
</script><div class="carousel">
    <div class="carousel__container">
        {#each images as image (image.id)}
            <img
                src={image.path}
                alt={image.alt}
                id={image.id}
                style={`height: ${imageHeight}px; margin-right: ${imageSpacing}px`}
            />
        {/each}
    </div>
</div>

<style>
    .carousel {
        display: flex;
        overflow-x: auto;
        position: relative;
        width: 100%;
    }
    .carousel__container {
        display: flex;
    }
</style>