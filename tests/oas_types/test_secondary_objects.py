import pytest

from sanic_openapi3e.oas_types import (
    XML,
    Contact,
    Discriminator,
    OAuthFlow,
    OAuthFlows,
    ServerVariable,
)

########################################################################################################################
# Discriminator
########################################################################################################################


def test_discriminator():
    assert Discriminator(
        property_name="name", mapping={"first": "FirstName", "last": "LastName"}
    ).as_yamlable_object() == {"mapping": {"first": "FirstName", "last": "LastName"}, "propertyName": "name"}

    with pytest.raises(AssertionError):
        Discriminator(property_name="name", mapping={"first": "FirstName", "last": "LastName", "contact": Contact})


########################################################################################################################
# OAuthFlows, OAuthFlow
########################################################################################################################


def test_oauthflows_keys_casing__issue9():
    assert OAuthFlows(
        authorization_code=OAuthFlow(
            authorization_url="authorization_url", token_url="token_url", scopes={"scope1": "", "scope2": ""},
        )
    ).as_yamlable_object() == {
        "authorizationCode": {
            "authorizationUrl": "authorization_url",
            "tokenUrl": "token_url",
            "scopes": {"scope1": "", "scope2": ""},
        }
    }


########################################################################################################################
# ServerVariable
########################################################################################################################


def test_servervariable():
    assert ServerVariable(
        default="prod", enum=["dev", "staging", "prod"], description="instance environment"
    ).as_yamlable_object() == {
        "default": "prod",
        "description": "instance environment",
        "enum": ["dev", "staging", "prod"],
    }

    with pytest.raises(AssertionError):
        not_a_str: int = 404
        ServerVariable(default="prod", enum=["dev", "staging", "prod", not_a_str], description="instance environment")

    with pytest.raises(AssertionError):

        ServerVariable(
            default="prod",
            enum=["dev", "staging", "prod", "repeated-env", "repeated-env"],
            description="instance environment",
        )


########################################################################################################################
# XML
########################################################################################################################


def test_xml():
    assert XML(name="name", namespace="ns", prefix="prefix", attribute=False, wrapped=False).as_yamlable_object() == {
        "name": "name",
        "namespace": "ns",
        "prefix": "prefix",
        "attribute": False,
        "wrapped": False,
    }
