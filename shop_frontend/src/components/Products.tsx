import { useState, useEffect } from "react";
import axios from "axios";

type Product = {
  id: number;
  name: string;
  description: string;
  stock: number;
  price: string; 
  category: string;
};

const Products = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/shop/products") 
      .then((response) => {
        setProducts(response.data);
        setLoading(false);
      })
      .catch((err) => {
        console.log(err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading products...</p>;
  }

  return (
    <div>
      <h2>Products</h2>
      {products.map((product) => (
        <div key={product.id}>
          <h3>{product.name}</h3>
          <p>
            <strong>Description:</strong> {product.description}
          </p>
          <p>
            <strong>Stock:</strong> {product.stock}
          </p>
          <p>
            <strong>Price:</strong> {product.price}
          </p>
          <p>
            <strong>Category:</strong> {product.category}
          </p>
        </div>
      ))}
    </div>
  );
};

export default Products;
