from fastapi import APIRouter
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router =  APIRouter(
    prefix= "/product",
    tags=["product"]
)

products =  ["watch" , "camera" , "phone" ]

@router.get("/all")
def get_all_products():
    # return products
    data = " ".join(products)
    return Response(content= data, media_type="text/plain")
@router.get("/{id}", responses= {
    200: {
        "content": {
            "text/html": {
                "example": "<div> Product </div>"
            }
            },
            "description": "Returns the HTML of product with id"
        },
    400: {
        "content": {
            "text/plain": {
                "example": "prodcuts not found"
            }
        },
        "description": "A clear text information that product was not found"
    }
            })
def get_product(id: int):
    
    if id > len(products) or id < 0:
        return PlainTextResponse(status_code=404, content= "Product not found", media_type="text/plain")
    else:
        product = products[id]
        out = f"""
                <head>
                    <style>
                    .product {{
                    width: 500px;
                    height: 30px;
                    border: 2px inset green;
                    background-color: lightblue;
                    text-align: center;
                    }}
                    </style>
                </head>
                <div class = "product"> {product} </div>
            """
    return HTMLResponse(content= out, media_type= "text/html")



