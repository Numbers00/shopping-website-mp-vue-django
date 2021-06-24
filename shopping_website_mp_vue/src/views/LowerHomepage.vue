<template>
<div>
<div class="container-xl p-5 m-5">
    <div class="mx-auto">
    <div class="row mx-auto m-5 offset-3" style="font-size: large; text-align: center; color:#ED8A61;">
    <br><br><br>
    <h1 style="font-family: fredoka one;">What do you want to do right now?</h1>
    </div>
    <div class="row mx-auto offset-3" style="font-size: large; width: 75vw; position: relative; left: 50%; transform: translate(-50%);">

        <div class="col-md p-3 m-auto offset-md-3 "  >
           <div class="item" :style="{'background-image': 'url(' + require('@/assets/img/gallery/books_dark.jpeg') + ')'}">
                <div class="panel">
                <h1><b>Rent or Buy a Book</b></h1>
                <p>Choose from our handpicked selection of books with reasonable prizes
                    <a @click="$router.push({ name: 'Books' })">here</a>
                </p>
            </div>
        </div>
        </div>

        <div class="col-md p-3 m-auto offset-1" >
            <div class="item" :style="{'background-image': 'url(' + require('@/assets/img/gallery/collaboration.jpg') + ')'}">
            <div class="panel">
                <h1><b>Tutorial Services</b></h1>
                <p>Having a hard time? Looking for a study buddy? Read about our study hub
                    <a @click="$router.push({ name: 'Tutors' })">here</a>
                </p>
            </div>
            </div>

        </div>

        <div class="col-md p-3 m-auto offset-1 " >
            <div class="item" :style="{'background-image': 'url(' + require('@/assets/img/gallery/kimchiFR.jpg') + ')'}">
            <div class="panel">
                <h1><b>About Us</b></h1>
                <p>Know more about the developers
                    <a @click="$router.push({ name: 'Tutors' })">here</a>
                </p>
            </div>
            </div>
        </div>
        <div class="col-md p-3 m-auto offset-1 " >
            <div class="item" :style="{'background-image': 'url(' + require('@/assets/img/gallery/donutcoffee.jpg') + ')'}">
            <div class="panel">
                <h1><b>Donuts & Coffee</b></h1>
                <p>
                Brew & Bake corner coming
                <a @click="$router.push({ name: 'Cafe' })">here</a>
                soon!
                </p>
            </div>
            </div>
        </div>
        </div>

    </div>
</div>

<div class="overlay1" style="top: 0%;"></div>
<div class="overlay2" style="top: 50%;"></div>
<div class="overlay1" style="top: 100%;"></div>

<div class="overlay3" ></div>
<div class="overlay4" ></div>
</div>
</template>

<script>

export default {
    name: 'LowerHomepage',
    mounted () {
        document.title = 'Home | Code & Chill'
    }
}
</script>

<style scoped src='@/assets/css/design.css'></style>
