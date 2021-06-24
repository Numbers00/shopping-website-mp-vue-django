<template>
<div id="contents" style="margin-bottom: 200px;">
 <div class="container px-2 px-md-4 py-5 mx-auto">
   <div class="row">
   <div class="col-12 border-0">
     <div class="row d-flex">
       <div class="col-lg-5">
         <div class="card1 pb-5">
           <div class="row px-3">
             <div class="col-12">
               <a
                 @click="$router.push({ name: 'Books' })"
                 style="text-align: right; text-decoration: none"
                 ><span
                   class="fa fa-home"
                   style="font-size: 2.5rem; color: white; padding-top: 20px"
                 ></span>
                 <span style="color: white; font-size: 1.5rem"
                   >&nbsp; Code&Chill</span
                 ></a
               >
             </div>
           </div>
           <div class="row px-3 justify-content-center mt-4 mb-5">
             <div
               id="carouselExampleIndicators"
               class="carousel slide"
               data-ride="carousel"
               data-interval="8000"
             >
               <ol class="carousel-indicators">
                 <li
                   data-target="#carouselExampleIndicators"
                   data-slide-to="0"
                   id="li1"
                 ></li>
                 <li
                   data-target="#carouselExampleIndicators"
                   data-slide-to="1"
                   id="li2"
                 ></li>
                 <li
                   data-target="#carouselExampleIndicators"
                   data-slide-to="2"
                   id="li3"
                   class="active"
                 ></li>
                 <li
                   data-target="#carouselExampleIndicators"
                   data-slide-to="3"
                   id="li4"
                 ></li>
                 <li
                   data-target="#carouselExampleIndicators"
                   data-slide-to="4"
                   id="li5"
                 ></li>
               </ol>
               <div class="carousel-inner">
                 <div class="carousel-item col-12 bg-light border-0 card-0">
                   <div class="text-center">
                     <img
                       src="https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png"
                       class="img-fluid profile-pic"
                     />
                   </div>
                   <h6 class="font-weight-bold mt-5">Federico Coscolluela</h6>
                   <small class="mb-2">Fed</small>
                   <hr width="50%" />
                   <p class="content mt-2 mb-0">
                     My full name is Jan Federico Coscolluela IV, also the fourth of us siblings. I am 20 years old and I like a cappella and country music. I'm also a huge fan of Mitch Albom and his novels.
                   </p>
                 </div>
                 <div class="carousel-item col-12 bg-light border-0 card-0">
                   <div class="text-center">
                     <img
                       src="https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png"
                       class="img-fluid profile-pic"
                     />
                   </div>
                   <h6 class="font-weight-bold mt-5">Beatrice Lapuz</h6>
                   <small class="mb-2">Rice</small>
                   <hr width="50%" />
                   <p class="content mt-2 mb-0">
                     Programmer by education, artist by heart. I like learning new languages and playing artsy games. Please support our project by having fun with it. Let the show begin!
                   </p>
                 </div>
                 <div class="carousel-item active col-12 bg-light border-0 card-0">
                   <div class="text-center">
                     <img
                       src="https://icons.iconarchive.com/icons/grafikartes/adobe-cc/128/CC-icon.png"
                       class="img-fluid profile-pic"
                     />
                   </div>
                   <h6 class="font-weight-bold mt-5" style="text-align: center;">Acads Meet Leisure</h6>
                   <p style="text-align: center;"><small class="mb-2">Who are we?</small></p>
                   <hr width="100%" />
                   <p class="content mt-2 mb-0" style="letter-spacing: 1px; text-align: center;">
                     If you're a passionate bibliophile like us (or just want to take a rest and immerse yourself in good reads). <br><br> Code&Chill got your back! Feel free to browse our selections.
                   </p>
                 </div>
                 <div class="carousel-item col-12 bg-light border-0 card-0">
                   <div class="text-center">
                     <img
                       src="https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png"
                       class="img-fluid profile-pic"
                     />
                   </div>
                   <h6 class="font-weight-bold mt-5">Beatrice Lapuz </h6>
                   <small class="mb-2">Rice</small>
                   <hr width="50%" />
                   <p class="content mt-2 mb-0">
                     Programmer by education, artist by heart. I like learning new languages and playing artsy games. Please support our project by having fun with it. Let the show begin!
                   </p>
                 </div>
                 <div class="carousel-item col-12 bg-light border-0 card-0">
                   <div class="text-center">
                     <img
                       src="https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png"
                       class="img-fluid profile-pic"
                     />
                   </div>
                   <h6 class="font-weight-bold mt-5">Kyle Aquino</h6>
                   <small class="mb-2">Kyle</small>
                   <hr width="50%" />
                   <p class="content mt-2 mb-0">
                     Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente praesentium impedit illum perspiciatis veritatis ullam adipisci laudantium nihil, dolor soluta.
                   </p>
                 </div>
               </div>
             </div>
           </div>
         </div>
       </div>
       <div class="col-lg-7">
         <div class="col-12 border-0 border-light px-4 px-sm-5 py-5" style="background-color: white; border-radius: 0 3% 3% 0;">
           <small class="text-right mb-3"
             ><a @click="$router.push({ name: 'Login' })"
               ><u>I already have an account</u></a
             ></small
           >
           <h3 class="mb-1" style="text-transform: uppercase; letter-spacing: 3px;">Sign up</h3>
           <p class="mb-4 text-sm">We're glad you're here with us today!</p>
           <form @submit.prevent="submitForm">
            <div class="row mt-3">
              <div class="col-md-6">
                <label class="mb-0">
                  <h6 class="mb-0 text-sm">Full Name</h6>
                </label>
                <input type="text" v-model="fullName" name="fname" placeholder="John Doe" required />
              </div>
              <div class="col-md-6">
                <label class="mb-0">
                  <h6 class="mb-0 text-sm">Phone Number</h6>
                </label>
                <input type="text" v-model="phone" name="number" placeholder="09457325869" required />
              </div>
            </div>
            <div class="row px-3">
              <label class="mb-0">
                <h6 class="mb-0 text-sm">Address</h6>
              </label>
              <input
                type="text"
                v-model="address"
                name="email"
                placeholder="Street Address, City, Province, Country"
                required
              />
            </div>
            <div class="row px-3">
              <label class="mb-0">
                <h6 class="mb-0 text-sm">Email</h6>
              </label>
              <input
                type="text"
                v-model="email"
                name="email"
                placeholder="john.doe@email.com"
                required
              />
            </div>
            <div class="row px-3">
              <label class="mb-0">
                <h6 class="mb-0 text-sm">Password</h6>
              </label>
              <input
                type="password"
                v-model="password"
                name="password"
                placeholder="&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;"
                required
              />
            </div>
            <div class="row px-3 mb-3">
              If you're okay with the details you have provided, you may now click the button below.
            </div>
            <div class="row mb-4">
              <div class="col-md-6">
                <button type="submit" class="btn btn-blue text-center mb-1 py-2">
                  Create Account
                </button>
              </div>
            </div>
           </form>
         </div>
       </div>
       </div>
     </div>
   </div>
 </div>
 <link
   href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
   rel="stylesheet"
 />
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data () {
    return {
      fullName: '',
      phone: '',
      email: '',
      password: '',
      address: ''
    }
  },
  mounted () {
    document.title = 'Signup | Code & Chill'
  },
  methods: {
    submitForm () {
      const formData = {
        full_name: this.fullName,
        username: this.email,
        phone: this.phone,
        email: this.email,
        address: this.address,
        password: this.password
      }

      axios
        .post('/api/v1/users/', formData)
        .then(response => {
        })
        .catch(error => {
          if (error.response) {
            console.log(JSON.stringify(error.response.data))
          } 
          else if (error.message) {
            console.log(JSON.stringify(error))
          }
        })

      axios
        .post('/api/v1/send_confirmation_email/', formData)
        .then(response => {
          this.$router.push('/login')
        })
        .catch(error => {
            console.log(error)
        })
    }
  }
}
</script>

<style scoped>

#contents {
  color: #000;
  overflow-x: hidden;
  height: 100%;
  background-color: #eeeeee;
  background-repeat: no-repeat;
  text-align: left;
}

#contents a {
  color: #000;
}

.card0 {
  box-shadow: 0px 4px 8px 0px #757575;
  border-radius: 20px;
}

.card1 {
  border-bottom-left-radius: 20px;
  border-top-left-radius: 20px;
  background: rgb(43, 42, 42);
  height: 100%;
  color: #fff;
  padding-left: 13%;
  padding-right: 13%;
}

.logo {
  margin-top: 30px;
  margin-left: 15px;
  cursor: pointer;
  text-decoration: none;
}

.card2 {
  border-bottom-right-radius: 20px;
  border-top-right-radius: 20px;
}

.social-connect .fa-home {
  color: #df4b37;
  padding: 10px 12px;
  font-size: 20px;
}

.social-connect .fa-facebook-square {
  color: #3b5998;
  padding: 10px 15px;
  font-size: 20px;
}

.social-connect {
  padding: 3px 0px 3px 3px;
  border-radius: 10px;
  cursor: pointer;
  border: 1px solid #e0e0e0;
}

.social-connect:hover {
  background-color: blue;
}

.line {
  height: 1px;
  width: 45%;
  background-color: #e0e0e0;
  margin-top: 10px;
}

.or {
  width: 10%;
}

.text-center {
  text-align: center;
}

.text-sm {
  font-size: 14px !important;
}

input {
  padding: 10px 12px 10px 12px;
  border: 1px solid lightgrey;
  border-radius: 10px;
  margin-bottom: 25px;
  margin-top: 2px;
  width: 100%;
  box-sizing: border-box;
  color: #2c3e50;
  font-size: 14px;
  letter-spacing: 1px;
}

input:focus {
  -moz-box-shadow: none !important;
  -webkit-box-shadow: none !important;
  box-shadow: none !important;
  border: 1px solid #512da8;
  outline-width: 0;
}

::placeholder {
  color: #eeeeee;
  opacity: 1;
}

:-ms-input-placeholder {
  color: #eeeeee;
}

::-ms-input-placeholder {
  color: #eeeeee;
}

button:focus {
  -moz-box-shadow: none !important;
  -webkit-box-shadow: none !important;
  box-shadow: none !important;
  outline-width: 0;
}

.btn-blue {
  background-color: #512da8;
  width: 100%;
  color: #fff;
  border-radius: 6px;
}

.btn-blue:hover {
  background-color: #311b92;
  color: #fff;
  cursor: pointer;
}

.card-0 {
  color: #311b92;
  background-color: #fff;
  border-radius: 20px;
  min-height: 352px;
  margin-top: 80px;
  padding: 30px;
}

.carousel-indicators {
  position: absolute;
  bottom: -100px;
  display: -webkit-box !important;
}

.carousel-indicators li {
  cursor: pointer;
  border-radius: 50% !important;
  width: 40px !important;
  height: 40px !important;
  opacity: 0.5;
  margin: 5px !important;
}

.carousel-indicators li.active {
  opacity: 1;
  width: 50px !important;
  height: 50px !important;
  margin-top: 0px !important;
  border: 2px solid #fff;
}

.carousel-indicators li#li1 {
  background: url("https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-group-icon.png") !important;
  background-size: cover !important;
  background-repeat: no-repeat;
  display: none;
}

.carousel-indicators li#li2 {
  background: url("https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png") !important;
  background-size: cover !important;
  background-repeat: no-repeat;
  display: none;
}

.carousel-indicators li#li3 {
  background: url("https://icons.iconarchive.com/icons/grafikartes/adobe-cc/128/CC-icon.png") !important;
  background-size: cover !important;
  background-repeat: no-repeat;
  display: none;
}

.carousel-indicators li#li4 {
  background: url("https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png") !important;
  background-size: cover !important;
  background-repeat: no-repeat;
  display: none;
}

.carousel-indicators li#li5 {
  background: url("https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png") !important;
  background-size: cover !important;
  background-repeat: no-repeat;
  display: none;
}

.profile-pic {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  position: absolute;
  top: -50px;
  left: calc(50% - 50px);
}

.content {
  color: #000;
  font-size: 14px;
}

.social {
  margin-top: 150px;
}

@media screen and (max-width: 991px) {
  .card1 {
    border-bottom-left-radius: 0px;
    border-top-right-radius: 20px;
  }

  .card2 {
    border-bottom-left-radius: 20px;
    border-top-right-radius: 0px;
  }
}

</style>
