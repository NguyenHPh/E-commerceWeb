
<template>
<div class="cart__table">
    <div class="table__item">

        <img v-bind:src="item.product.get_image">
        <div class="item__info">
            <router-link :to="item.product.get_absolute_url" class = "info--name">{{ item.product.brief_component }}</router-link>
            <p class = "info--age">{{ item.product.lifeStage }}+ / {{ item.product.get_trays[0][1] }} trays</p>
        </div>
    </div>
    <div class="table__price">
        <div class="price__product">
            <p class = "price__product--total">£{{ item.product.get_trays[0][0]*item.product.get_trays[0][1] }}</p>
            <p class = "price__product--per-kg">£{{ item.product.get_trays[0][0] }} per tray</p>
        </div>
    </div>
    <div class="table__qty">
        <form action="" method="post">
            <i class="fa fa-minus" @click="decrementQuantity(item)"></i>
            <input type="number" name = "product-quantity" min="1" v-model="item.quantity">
            <i class="fa fa-plus" @click="incrementQuantity(item)"></i>
        </form>
    </div>
    <div class="table__subtotal">
        <p class = "subtotal--content" style="text-align:center;">£{{ getItemTotal(item) }}</p>
    </div>
    <div class="table__delete">
        <a class = "delete--x" @click="removeFromCart(item)" ><i class="fas fa-times"></i></a>
        <a href="" class = "delete--remove">Remove</a>
    </div>
</div>
</template>


                        

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.product.get_trays[0][0]*item.product.get_trays[0][1]*item.quantity
        },
        decrementQuantity(item) {
            item.quantity -= 1

            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }

            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1

            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)

            this.updateCart()
        },
    },
}
</script>

<style>
    .table__item img{
        width: 120px;
        height: auto;
        margin-right: 20px;
    }


    input::-webkit-outer-spin-button,
    input::-webkit-inner-spin-button {
      -webkit-appearance: none;
      margin: 0;
    }

    /* Firefox */
    input[type=number] {
      -moz-appearance: textfield;
      margin-left: 5px;
      margin-right: 5px;
    }

    .fa-minus, .fa-plus, .delete--x{
        cursor: pointer;
    }
    
    .item__info a:hover{
        color: #2C7328;
    }
</style>