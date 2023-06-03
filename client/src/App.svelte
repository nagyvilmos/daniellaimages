<script>
  import Carousel from './components/Carousel.svelte';
  const images = [
      {
          path: 'https://picsum.photos/id/1012/3973/2639',
          id: 'man-dog',
          alt: 'A man with his faithless dog',
      },
      {
          path: 'https://picsum.photos/id/1005/5760/3840',
          id: 'looking',
          alt: 'Looking out to sea to see what he can see at sea',
      },
      {
          path: 'https://picsum.photos/id/1020/4288/2848',
          id: 'bear',
          alt: 'A large smelly bear',
      },
      {
          path: 'https://picsum.photos/id/1025/4951/3301',
          id: 'dog',
          alt: 'dog in a blanket',
      },
      {
          path: 'https://picsum.photos/id/103/2592/1936',
          id: 'field-feet',
          alt: 'Feet in a field',
      },
      {
          path: 'https://picsum.photos/id/104/3840/2160',
          id: 'sky-hook',
          alt: 'Some arty thing hanging from the sky',
      },
  ];
</script>
<main>
  <h2 class="item__title">Daniella Images</h2>
  <div class="item__gallery">
      <Carousel {images} />
  </div>
  <p class="item__description">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae ipsum
      possimus accusamus aut, assumenda fuga labore provident, non molestiae
      recusandae harum, fugit neque nisi quos qui nulla. Non, quaerat officia.
  </p>
</main>
<style>
  main {
      padding: 1em;
      max-width: 800px;
      margin: 0 auto;
  }
</style>