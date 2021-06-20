<template>
<div>
  <ul class="bs4-order-tracking">
    <li class="step active" style="font-size: 12px;">
      <div><i class="fa fa-user"></i></div>
      <a @click="$router.push({ name: 'Books' })" style="text-decoration: none; color: inherit">Shop More</a>
    </li>
    <li class="step active" style="font-size: 12px;">
      <div><i class="fa fa-user"></i></div>
      <a @click="$router.push({ name: 'Cart' })" style="text-decoration: none; color: inherit">Cart</a>
    </li>
    <li class="step active" style="font-size: 12px;">
      <div><i class="fa fa-money"></i></div>
      Payment
    </li>
    <li class="step" style="font-size: 12px;">
      <div><i class="fa fa-truck"></i></div>
      Delivery
    </li>
  </ul>
  <div class="row mb-4">
    <div class="col-lg-8 mx-auto text-center">
      <h4 class="title">Payment</h4>
    </div>
  </div>
  <div class="d-flex flex-row" style="display: block; margin: auto; max-width: 80%; justify-content: center;">
    <div class="container py-5 col-8 position-relative" style="flex-grow: 1; width: 1200px; left: 200px;">
      <br>
      <!-- End -->
      <div class="row">
        <div class="col-md-7 col-12">
          <div class="payment-card" :class="{'body-cash-size': cashToggle, 'cover-credit-size': creditToggle}">
            <div class="card-header" :class="{'cover-cash-size': cashToggle, 'cover-credit-size': creditToggle}">
              <div class="bg-white shadow-sm pt-4 pl-2 pr-2 pb-2">
                <!-- Credit card form tabs -->
                <ul role="tablist" class="nav bg-light nav-pills rounded nav-fill mb-3">
                  <li class="nav-item"> <a @click="handleClickCredit" data-toggle="pill" href="#credit-card" class="nav-link active "> <i
                        class="fa fa-credit-card mr-2"></i> Credit Card </a> </li>
                  <li class="nav-item"> <a @click="handleClickCash" data-toggle="pill" href="#COD" class="nav-link "> <i
                        class="fa fa-money mr-2"></i> Cash On Delivery </a> </li>
                </ul>
              </div> <!-- End -->
              <!-- Credit card form content -->
              <div class="tab-content">
                <!-- credit card info-->
                <div id="credit-card" v-if="creditToggle" class="tab-pane fade show active pt-3">
                  <form role="form" onsubmit="event.preventDefault()">
                    <div class="form-group mb-3"> <label for="username">
                        <h6>Card Owner</h6>
                      </label> <input type="text" name="username" placeholder="Card Owner Name" required
                        class="form-control "> </div>
                    <div class="form-group mb-3"> <label for="cardNumber">
                        <h6>Card Number</h6>
                      </label>
                      <div class="input-group"> <input type="text" name="cardNumber" placeholder="Valid card number"
                          class="form-control " required>
                        <div class="input-group-append"> <span class="input-group-text text-muted"> <i
                              class="fa fa-cc-visa mx-1"></i> <i class="fa fa-cc-mastercard mx-1"></i> <i
                              class="fa fa-cc-amex mx-1"></i> </span> </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-8">
                        <div class="form-group mb-3"> <label><span class="hidden-xs">
                              <h6>Expiration Date</h6>
                            </span></label>
                          <div class="input-group"> <input type="number" placeholder="MM" name="" class="form-control"
                              required> <input type="number" placeholder="YY" name="" class="form-control" required>
                          </div>
                        </div>
                      </div>
                      <div class="col-sm-4">
                        <div class="form-group mb-4"> <label data-toggle="tooltip"
                            title="Three digit CV code on the back of your card">
                            <h6>CVV <i class="fa fa-question-circle d-inline"></i></h6>
                          </label> <input type="text" required class="form-control"> </div>
                      </div>
                    </div>
                    <div class="card-footer"> <button type="button" class="subscribe btn btn-primary btn-block shadow-sm"
                        style="float: right;"><a href="summary.html" style="text-decoration: none; color: inherit;">
                          Confirm Payment</a> </button>
                    </div>
                  </form>
                </div>
              </div> <!-- End -->
              <!-- Paypal info -->
              <div id="COD" v-if="cashToggle" class="tab-pane fade pt-3">
                <h6 class="pb-2">Kindly provide your details below.</h6>
                <form role="form" onsubmit="event.preventDefault()">
                  <div class="form-group mb-3"> 
                    <label for="username">
                      <h6>Full Name</h6>
                    </label> 
                    <input type="text" name="username" placeholder="Sheldon Cooper" class="form-control" required> 
                  </div>
                  <div class="form-group mb-3"> 
                    <label for="username">
                      <h6>Complete Address</h6>
                    </label> 
                    <input type="text" name="cardNumber" placeholder="Street Address, City, Province, Country" class="form-control" required> 
                  </div>
                  <div class="row">
                    <div class="col-sm-6">
                      <div class="form-group mb-3"> <label><span class="hidden-xs">
                            <h6>Contact Number</h6>
                          </span></label>
                        <div class="input-group"> <input type="number" placeholder="09457325869" name=""
                            class="form-control" required> </div>
                      </div>
                    </div>
                    <div class="col-sm-6">
                      <div class="form-group mb-4"> <label>
                          <h6>Email Address</h6>
                        </label> <input type="text" required class="form-control" placeholder="someone@gmail.com"> </div>
                    </div>
                  </div>
                  <div class="card-footer"> <button type="button" class="subscribe btn btn-primary btn-block shadow-sm"
                      style="float: right;"><a @click="$router.push({ name: 'Summary' })" style="text-decoration: none; color: inherit;">
                        Confirm Payment</a> </button>
                  </div>
                </form>
              </div> <!-- End -->
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-md-5 col-4 position-relative" style="flex-grow: 1; top: 80px; right: 240px;">
      <img src="@/assets/img/illustrations/codinggif.gif" width="450px"
        style="margin-left: auto; margin-right: auto; margin-top: 25px;" alt="">
    </div>
  </div>
</div>
</template>

<script>

export default {
    name: 'Payment',
    data () {
      return {
        creditToggle: true,
        cashToggle: false
      }
    },
    methods: {
      handleClickCredit () {
        if (!this.creditToggle) {
          this.creditToggle = true
          this.cashToggle = false
        }
      },
      handleClickCash () {
        if (!this.cashToggle) {
          this.cashToggle = true
          this.creditToggle = false
        }
      }
    }
}
</script>

<style>
body {
  background-color: white !important;
}
</style>

<style scoped src='@/assets/css/payment.css'>
.body-credit-size {
  height: 480px;
}
.cover-credit-size {
  height: 430px;
}
.body-cash-size {
  height: 570px;
}
.cover-cash-size {
  height: 550px;
}
</style>