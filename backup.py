from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("trial.html")


if __name__ == "__main__":
    app.run(debug=True)

# header.masthead {
#   position: relative;
#   margin-bottom: 3rem;
#   padding-top: calc(8rem + 57px);
#   padding-bottom: 8rem;
#   background: no-repeat center center;
#   background-color: #6c757d;
#   background-size: cover;
#   background-attachment: scroll;

 #

 # <button type="button" data-bs-target="#tino-carousel" data-bs-slide-to="6" aria-label="Slide 7"></button>
 #                      <button type="button" data-bs-target="#tino-carousel" data-bs-slide-to="7" aria-label="Slide 8"></button>
 #                      <button type="button" data-bs-target="#tino-carousel" data-bs-slide-to="8" aria-label="Slide 9"></button>



# carouselExampleIndicators

