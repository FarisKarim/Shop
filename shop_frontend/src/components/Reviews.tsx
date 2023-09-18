import { useState, useEffect } from "react";
import axios from "axios";

type Review = {
    id: number;
    rating: number;
    comment: string;
    title: string;
    created_at: string;
    user_display: string;
    product_display: string;
};



const Reviews = () => {
  const [reviews, setReviews] = useState<Review[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/shop/reviews")
      .then((res) => {
        setReviews(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.log(err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading reviews...</p>;
  }

  return (
    <div>
      <h2>Reviews</h2>
      {reviews.map((review) => (
        <div key={review.id}>
          <h3>{review.title}</h3>
          <p>
            <strong>Rating:</strong> {review.rating} / 5
          </p>
          <p>
            <strong>Comment:</strong> {review.comment}
          </p>
          <p>
            <strong>User:</strong> {review.user_display}
          </p>
          <p>
            <strong>Product:</strong> {review.product_display}
          </p>
          <p>
            <small>Created at: {review.created_at}</small>
          </p>
          <hr />
        </div>
      ))}
    </div>
  );
};

export default Reviews;
