"""Add last few columns to posts table

Revision ID: 5edc480bf5f9
Revises: 274102f6b508
Create Date: 2022-03-23 11:51:33.552156

"""
from http import server
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5edc480bf5f9'
down_revision = '274102f6b508'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)

    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
