from typing import Set

from sanic_openapi3e.oas_types import Contact, License, PathItem, Paths, Tag

########################################################################################################################
# Contact
########################################################################################################################


def test_contact():
    contact = Contact(name="name", url="www.url.com", email="email@url.com")
    assert contact.serialize() == {
        "name": "name",
        "url": "www.url.com",
        "email": "email@url.com",
    }
    assert contact.as_yamlable_object() == {
        "name": "name",
        "url": "www.url.com",
        "email": "email@url.com",
    }


########################################################################################################################
# License
########################################################################################################################


def test_license():
    _license = License(name="name", url="www.url.com")
    assert _license.serialize() == {"name": "name", "url": "www.url.com"}


########################################################################################################################
# Paths, PathItem
########################################################################################################################


def test_pathitem():
    pi = PathItem(x_exclude=True)
    assert pi.x_exclude

    ps = Paths([("test_pathitem", pi)])
    pi = ps["test_pathitem"]
    assert pi.x_exclude


########################################################################################################################
# Tag
########################################################################################################################


def test_tag_eq():
    tag = Tag("name", "desc")
    assert tag == tag
    assert tag == Tag("name", "desc")


def test_set_of_tags():
    tags: Set[Tag] = set()
    tags.add(Tag("name", "desc"))
    tags.add(Tag("name", "desc"))
    assert len(tags) == 1, tags


def test_sorted_tags():
    tags: Set[Tag] = set()
    tags.add(Tag("nameB", "descB"))
    tags.add(Tag("nameA", "descA"))
    assert sorted(tags) == [Tag("nameA", "descA"), Tag("nameB", "descB")]
