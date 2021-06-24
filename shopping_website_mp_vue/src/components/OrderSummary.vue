<template>
    <div style="margin-bottom: 20px;">
        <h6 style="text-align: left; margin-left: 20px;"><b>Order #{{ order.id }}</b></h6>

        <table style="width: 100%;">
            <thead>
                <tr>
                    <th>Book</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Total</th>
                </tr>
            </thead>

            <tbody>
                <tr
                    v-for="item in order.items"
                    v-bind:key="item.book.id"
                >
                    <td class="book-title">{{ item.book.title }}</td>
                    <td>${{ item.book.price }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>${{ getItemTotal(item).toFixed(2) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'OrderSummary',
    props: {
        order: Object
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.book.price
        },
        orderTotalLength(order) {
            return order.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
    }
}
</script>

<style scoped>
tr:nth-child(even) {
  background-color: #f2f2f2;
}
.book-title {
  min-width: 50%;
  max-width: 50%;
  width: 50%;
}
</style>