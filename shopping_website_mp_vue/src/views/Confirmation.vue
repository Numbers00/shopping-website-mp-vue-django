<template>
<div>
    <div class="face">
        <div class="band">
            <div class="green"></div>
            <div class="white"></div>
            <div class="blue"></div>
        </div>
        <div class="eyes"></div>
        <div class="dimples"></div>
        <div class="mouth"></div>
    </div>

    <p style="font-size: 1.4rem; text-align: center; padding-top: 10px; font-family: quicksand;">Package Confirmed! Hope
        you
        enjoy the book :)
    </p>
    <a @click="$router.push({ name: 'Books' })" style="text-decoration: none; color: inherit;">
        <div class="btn" style="font-family: quicksand;"> Return to
            Home
        </div>
    </a>
</div>
</template>

<script>

export default {
    name: 'Confirmation',
    mounted () {
        document.title = 'Order Confirmed! | Code & Chill'
    }
}
</script>

<style scoped src='@/assets/css/confirmation.css'>
</style>