﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using DG.Tweening;

public class Bullet : MonoBehaviour
{
    public SpriteRenderer bulletSprite;

    public void StartMove(Vector2 _createPos, Sprite _bulletSprite = null)
    {
        if (_bulletSprite == null)
        {
            _bulletSprite = bulletSprite.sprite;
        }

        bulletSprite.sprite = _bulletSprite;

        gameObject.SetActive(true);
        transform.position = _createPos;

        transform
            .DOMove(new Vector2(_createPos.x, 8f), 1f)
            .OnComplete(()=> {
                gameObject.SetActive(false);
            });
    }
}
