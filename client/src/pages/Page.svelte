<script>
    import Header from "../components/Header.svelte";
    import Footer from "../components/Footer.svelte";
</script>

<div>
    <Header />
    <div style="height: 64px;"/>
    <slot/>
    <Footer />
</div>
