import Head from "next/head";

import Layout from "../components/layout";
import Jumbotron from "../components/jumbotron";
import FourUp from "../components/4-up";
import MainGallery from "../components/main-gallery";
import Testimonials from "../components/testimonials";
import Pricing from "../components/pricing";

import { getPageData } from "../lib/api";
import { CMS_NAME } from "../lib/constants";
import { Basic } from "./post";

export default function ProductsPage({ page }) {
  return (
    <>
      <Layout>
        <Head>
          <title>Products | {CMS_NAME}</title>
        </Head>
        <Jumbotron
          title={page.title}
          subtitle={page.subtitle}
          imageUrl={page.image}
        />
        <Pricing
          heading={page.pricing.heading}
          description={page.pricing.description}
          plans={page.pricing.plans}
        />
        <Jumbotron
          title="Vous pouvez également vendre un ancien téléphone"
          subtitle="Merci de remplir ce formulaire"
          imageUrl={page.image}
        />
        <div className="mw7 center" style={{ marginTop: "2rem" }}>
          <h2 className="f2 b lh-title mb3"></h2>
          <p className="mw6"></p>
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <div>
              <div className="ph1-l w-100-l">
                <fieldset>
                  <input
                    placeholder="marque de telephone"
                    className="w-100 mb2"
                  />
                  <label htmlFor="email">Mark</label>
                </fieldset>
              </div>
              <div className="ph1-l w-100-l">
                <fieldset>
                  <input placeholder="description" className="w-100 mb2" />
                  <label htmlFor="email">description</label>
                </fieldset>
              </div>
            </div>
            <div
              style={{
                background: "#EBE7E6",
                opacity: "0.7",
                border: "1px dashed black",
                width: "50%",
              }}
            >
              <Basic bool="sszs" />
            </div>
          </div>
          <div
            style={{
              width: "100%",
              margin: "3rem auto",
              display: "flex",
              justifyContent: "center",
            }}
          >
            <button
              style={{
                fontSize: "1rem",
                margin: "0.5rem",
                padding: "1rem",
                background: "#44ad44",
                color: "white",
              }}
            >
              Envoyer les informations
            </button>
          </div>
        </div>
      </Layout>
    </>
  );
}

export async function getStaticProps() {
  const page = getPageData("products");
  return {
    props: { page },
  };
}
